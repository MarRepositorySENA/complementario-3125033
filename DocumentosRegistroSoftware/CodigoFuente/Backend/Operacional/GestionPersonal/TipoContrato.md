```
//ENTITY TIPOCONTRATO
package com.persona.Backend.Entity.Operational.GestionPersonal;

import com.persona.Backend.Entity.BaseEntity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;

@Entity
@Table(name="tipo_contrato")
public class TipoContrato extends BaseEntity {

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@Column(name = "nombre", length = 45, nullable = false)
	private String nombre;

	@Column(name = "cantidad_hora", nullable = false)
	private Integer cantidadHora;

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public Integer getCantidadHora() {
		return cantidadHora;
	}

	public void setCantidadHora(Integer cantidadHora) {
		this.cantidadHora = cantidadHora;
	}
	
	
}
//IREPOSITORY TIPOCONTRATO
package com.persona.Backend.IRepository.Operational.GestionPersonal;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.GestionPersonal.TipoContrato;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface ITipoContratoRepository extends IBaseRepository<TipoContrato, Long>{

}
//ISERVICE TIPOCONTRATO
package com.persona.Backend.IService.Operational.GestionPersonal;

import com.persona.Backend.Entity.Operational.GestionPersonal.TipoContrato;
import com.persona.Backend.IService.IBaseService;

public interface ITipoContratoService extends IBaseService<TipoContrato> {

}
//SERVICE TIPOCONTRATO
package com.persona.Backend.Service.Operational.GestionPersonal;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.GestionPersonal.TipoContrato;
import com.persona.Backend.IService.Operational.GestionPersonal.ITipoContratoService;
import com.persona.Backend.Service.BaseService;

@Service
public class TipoContratoService extends BaseService<TipoContrato> implements ITipoContratoService{

}
//CONTROLLER TIPOCONTRATO
package com.persona.Backend.Controller.Operational.GestionPersonal;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.GestionPersonal.TipoContrato;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/gestion_personal/tipo_contrato")
public class TipoContratoController extends BaseController<TipoContrato>{

}

```