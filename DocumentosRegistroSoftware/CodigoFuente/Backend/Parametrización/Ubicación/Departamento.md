```
//ENTIDAD DEPARTAMENTO
package com.persona.Backend.Entity.Parameter.Ubicacion;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "departamento")
public class Departamento extends BaseEntity {

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@ManyToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "pais_id", nullable = false, unique = false)
	private Pais paisId;

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public Pais getPaisId() {
		return paisId;
	}

	public void setPaisId(Pais paisId) {
		this.paisId = paisId;
	}

}
//IREPOSITORY DEPARTAMENTO
package com.persona.Backend.IRepository.Parameter.Ubicacion;

import java.util.Optional;
import com.persona.Backend.Entity.Parameter.Ubicacion.Departamento;
import com.persona.Backend.IRepository.IBaseRepository;

public interface IDepartamentoRepository extends IBaseRepository<Departamento, Long>{

	Optional<Departamento> findByNombre(String nombre);
}
//ISERVICE DEPARTAMENTO
package com.persona.Backend.IService.Parameter.Ubicacion;

import com.persona.Backend.Entity.Parameter.Ubicacion.Departamento;
import com.persona.Backend.IService.IBaseService;

public interface IDepartamentoService extends IBaseService<Departamento>{

	Departamento findByNombre(String nombre);
}
//SERVICE DEPARTAMENTO
package com.persona.Backend.Service.Parameter.Ubicacion;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Parameter.Ubicacion.Departamento;
import com.persona.Backend.IRepository.Parameter.Ubicacion.IDepartamentoRepository;
import com.persona.Backend.IService.Parameter.Ubicacion.IDepartamentoService;
import com.persona.Backend.Service.BaseService;

@Service
public class DepartamentoService extends BaseService<Departamento> implements IDepartamentoService {


    @Autowired
    private IDepartamentoRepository departamentoRepository;

    @Override
    public Departamento findByNombre(String nombre) {
        return departamentoRepository.findByNombre(nombre).orElse(null);
    }
}
//CONTROLLER DEPARTAMENTO
package com.persona.Backend.Controller.Parameter.Ubicacion;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Parameter.Ubicacion.Departamento;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/parameter/ubicacion/departamento")
public class DepartamentoController extends BaseController<Departamento>{

}

```